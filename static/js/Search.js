function Map_create() {
    //Creating new google.maps.Map object (google.maps.Map(mapDiv, options))
    var deliver;
    var data;

    var abc = new google.maps.LatLng(20.68177501, -103.3514794);

    var mapOptions = {
          center: abc,
          zoom: 15,
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    data = new google.maps.InfoWindow();
    
    var locationBlock = new google.maps.InfoWindow({map: map});//Creating an InfoWindow object (params = which map to put it on)
    
    if (navigator.geolocation) {
        
        navigator.geolocation.getCurrentPosition(function(position) {//"returns" a Position object, which has a Coordinates object within it
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            }

            locationBlock.setPosition(pos);
            locationBlock.setContent('You are Here!'); //need to make text black
            map.setCenter(pos);

/* ~~~~~~~~~~~~~~~~~  ON CLICK OF BUTTON ~~~~~~~~~~~~~~~~~~~~~~~~ */
            deliver = new google.maps.places.PlacesService(map);
            map.addListener('idle', performSearch);

        });//getCurrentPosition



/* ~~~~~~~~~~~~~~~~~~~~ PERFORM THE QUERY ~~~~~~~~~~~~~~~~~~~~~~~~~ */
        function performSearch() {
            var request = {
                bounds: map.getBounds(),
                keyword: 'library'
            }
            deliver.radarSearch(request, callback);
        }


/* ~~~~~~~~~~~~~~~~~~~~~~ ADD MARKERS TO MAP OF QUERY ~~~~~~~~~~~~~~~~~ */ 
        function callback(results, status) {
            if (status !== google.maps.places.PlacesServiceStatus.OK) {
                console.error(status);
            return;
            }
            for (var i = 0, result; result = results[i]; i++) {
              addMarker(result);
            }
        }


/* ~~~~~~~~~~~~~~~~~~~~~ ACTUALLY ADD MARKERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
        function addMarker(place) {
            var marker = new google.maps.Marker({
                map: map,
                position: place.geometry.location,
                icon: {
                    url: 'http://maps.gstatic.com/mapfiles/circle.png',
                    anchor: new google.maps.Point(10, 10),
                    scaledSize: new google.maps.Size(10, 17)
                }
              });

                google.maps.event.addListener(marker, 'click', function() {
                    deliver.getDetails(place, function(result,status) {
                        if(status !== google.maps.places.PlacesServiceStatus.OK) {
                        console.error(status);
                            return;
                        }
                    data.setContent(result.name);
                    data.open(map,marker);
      
              });
            });
         }
      }  


        


} //Map_create() end!





           
