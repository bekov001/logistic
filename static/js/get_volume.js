$("#count").click(function () {
    var value1 = parseInt($("#1").val());
    var value2 = parseInt($("#2").val());
    var value3 = parseInt($("#3").val());
    result = value1 * value2 * value3 / 1000000;
    $("#result").val(result);
    console.log(result)
})