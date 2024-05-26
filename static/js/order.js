const deliveryMethodOptions = document.getElementsByName("delivery_method")
const tableButton = document.getElementById("id_delivery_method_1");

console.log("connected")

for (let option of deliveryMethodOptions) {
    option.addEventListener("click", (e) => {
        if (tableButton.checked) {
            console.log("table button checked")
            document.getElementById("id_table_number").style.display = "block";
            document.getElementById("id_table_number").required = true;
        }
        else{
            console.log("table button not checked")
            document.getElementById("id_table_number").style.display = "none";
            document.getElementById("id_table_number").required = false;
        }
    })
}