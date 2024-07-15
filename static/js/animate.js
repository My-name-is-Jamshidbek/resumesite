$(document).ready(function(){
    $(".about_text-title").waypoint(function(){
        $(".about_text-title").addClass(
            "animate__animated animate__slideInDown"
        )
    }, {offset:'80%'})
    $("#intro").waypoint(function(){
        $("#intro").addClass(
            "animate__animated animate__flipInX"
        )
    }, {offset:'80%'})
    $("#animete_service").waypoint(function(){
        $("#animete_service").addClass(
            "animate__animated animate__zoomIn"
        )
    }, {offset:'80%'})
    $("#about_content-img").waypoint(function(){
        $("#about_content-img").addClass(
            "animate__animated animate__lightSpeedInLeft"
        )
    }, {offset:'80%'})
    $(".about_content-text").waypoint(function(){
        $(".about_content-text").addClass(
            "animate__animated animate__lightSpeedInRight"
        )
    }, {offset:'80%'})
    $(".service_icon").waypoint(function(){
        $(".service_icon").addClass(
            "animate__animated animate__zoomInUp"
        )
    }, {offset:'80%'})
    $(".portfolio-item").waypoint(function(){
        $(".portfolio-item").addClass(
            "animate__animated animate__backInUp"
        )
    }, {offset:'80%'})
})