function initMap() {
   var options = {
      zoom:10,
      center: { lat:40.730610, lng:-73.935242} //Coordinates of New York 
   }
var map = new google.maps.Map(document.getElementById('map'), options);
var marker = new google.maps.Marker({
   position:{lat: 40.6782, lng: -73.9442}, // Brooklyn Coordinates
   map:map, //Map that we need to add
   icon:'https://img.icons8.com/fluent/48/000000/marker-storm.png',
   // adding custom icons (Here I used a Flash logo marker)
   draggarble: false// If set to true you can drag the marker
});

var information = new google.maps.InfoWindow({
   content: '<h4>The marker is at Brooklyn</h4>'
});

marker.addListener('click', function() {
   information.open(map, marker);
});

}