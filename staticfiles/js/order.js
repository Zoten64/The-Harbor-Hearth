//The delivery option radio buttons
const deliveryMethodOptions = document.getElementsByName("delivery_method");
//Table delivery option
const tableButton = document.getElementById("id_delivery_method_1");

// Check on page load. If the user has scanned a
// QR-code the table number field should show.
// The code below this snippet only works on a button click
if (tableButton.checked) {
    tableNumberShow();
}

//Check if a delivery option button has been clicked
for (let option of deliveryMethodOptions) {
    option.addEventListener("click", (e) => {
        if (tableButton.checked) {
            tableNumberShow();
        }
        else{
            tableNumberHide();
        }
    });
}

function tableNumberShow(){
    /**
     * When this function is run the table
     * number field will show and be required
     */
    document.getElementById("id_table_number").style.display = "block";
    document.getElementById("id_table_number").required = true;
}

function tableNumberHide(){
    /**
     * When this function is run the table
     * number field will be hidden and not required
     */
    document.getElementById("id_table_number").style.display = "none";
    document.getElementById("id_table_number").required = false;
}