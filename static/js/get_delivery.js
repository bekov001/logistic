var data;

$("#weight").on("input", () => {
    let i = 0
    for (; i < data["info"].length; i++) {
    if ($("#delivery_type-" + i).is(":checked")) {
        func(i)
        break;
    }
}})
// async function getData(){
//     let url = "http://192.168.1.57:5000/api/weight_info"`
//     let response = await fetch(url)
//     return await response.json()
// }
function func(index) {
    // let data = await getData()
    let result;
    let value =  data["info"][index][1];
    let price = data["info"][index][2];
    let volume = parseFloat($("#result").val());
    let weight = parseFloat($("#weight").val());
    let volume_weight = volume * value;
    if (weight > volume_weight){
        result =  Math.round(price * weight / value).toFixed(3)
    } else {
        result = Math.round(price * volume).toFixed(3)
    }
    $("#delivery_price").val(result);
    console.log()
}
$.getJSON("http://192.168.1.57:5000/api/weight_info", function (json) {
    put_variable(json)
    }
);
function put_variable(json){
    window.data = json;
    console.log(data)
}
