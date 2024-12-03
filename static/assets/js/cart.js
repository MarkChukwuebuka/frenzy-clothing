// Check if button pressed
$(document).on('click', '#add-cart', function(e){
    e.preventDefault();
    const url = $(this).data('url');
    const productId = $(this).val();
    const productQty = $('#qty-cart').val();

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            product_id: $('#add-cart').val(),
            product_qty: productQty,
            csrfmiddlewaretoken: csrfToken,
            action: 'add'
        },

        success: function(json){
//            console.log(json)
//            document.getElementById("cart_quantity").textContent = json.qty
            location.reload();
        },

        error: function(xhr, errmsg, err){

        }
    });
})



// Delete Item From Cart
$(document).on('click', '.delete-product', function(e){
  e.preventDefault();

  const url = $(this).data('url');
  const productId = $(this).data('index');


  $.ajax({
  type: 'POST',
  url: url,
  data: {
    product_id: productId,
    csrfmiddlewaretoken: csrfToken,
    action: 'remove'
  },
  success: function(json){
      //console.log(json)
//      document.getElementById("cart_quantity").textContent = json.qty
      location.reload();
  },

  error: function(xhr, errmsg, err){

  }


  });

})




document.addEventListener('DOMContentLoaded', function () {
    // Select all elements with class 'qtyminus' and 'qtyplus'
    document.querySelectorAll('.qtyminus').forEach(function (element) {
        element.addEventListener('click', function (e) {
            e.preventDefault();
            var input = this.parentElement.querySelector('input.input-qty');
            var currentValue = parseInt(input.value);
            var productId = input.id.replace('select', ''); // Extract product ID from input field ID

            if (!isNaN(currentValue) && currentValue > 1) {
                input.value = currentValue - 1;
            } else {
                input.value = 1; // Prevent going below 1
            }

            updateCart(productId, input.value); // Trigger the update after decrement
        });
    });

    document.querySelectorAll('.qtyplus').forEach(function (element) {
        element.addEventListener('click', function (e) {
            e.preventDefault();
            var input = this.parentElement.querySelector('input.input-qty');
            var currentValue = parseInt(input.value);
            var productId = input.id.replace('select', ''); // Extract product ID from input field ID

            if (!isNaN(currentValue)) {
                input.value = currentValue + 1;
            } else {
                input.value = 1; // If the input value is not a number, set it to 1
            }

            updateCart(productId, input.value); // Trigger the update after increment
        });
    });
});

$(document).on('click', '.update-cart', function(e) {
    e.preventDefault();

    // grab the product id and update URL
    var productId = $(this).data('index');
    var updateUrl = $(this).data('url');

    $.ajax({
        type: 'POST',
        url: updateUrl,  // Use the URL retrieved from the data-url attribute
        data: {
            product_id: productId,
            product_qty: $('#select' + productId).val(), // Gets the value from the input
            csrfmiddlewaretoken: csrfToken,
            action: 'update'
        },
        success: function(json){
            console.log("success")
            location.reload();
        },
        error: function(xhr, errmsg, err){
            // Handle errors
            console.log("error")
        }
    });
});
