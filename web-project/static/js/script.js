"use strict";

// ВЕРХНЯЯ ФОРМА
const product = {
  products: [
    {
      productName: "1",
      productPrice: 200,
    },
    {
      productName: "2",
      productPrice: 700,
    },
    {
      productName: "3",
      productPrice: 400,
    },
    {
      productName: "4",
      productPrice: 900,
    },
    {
      productName: "5",
      productPrice: 100,
    },
  ],
};
const productInputName = document.querySelector(
  ".tab-content-input_product-name"
);
for (let i = 0; i < product.products.length; i++) {
  productInputName.insertAdjacentHTML(
    "beforeend",
    `<option value="${product.products[i].productName}" class="product-option">${product.products[i].productName}</option>`
  );
}
let productInputOption = document.querySelectorAll(".product-option");
let productInputCount = document.querySelector(
  ".tab-content-input_product-count"
);
let productInputPrice = document.querySelector(
  ".tab-content-input_product-price"
);
productInputName.addEventListener("change", function () {
  productInputCount.value = "";
  productInputPrice.value = "";
});
productInputCount.addEventListener("change", function () {
  for (let i = 0; i < product.products.length; i++) {
    if (productInputOption[i].selected) {
      productInputPrice.value =
        productInputCount.value * product.products[i].productPrice;
    }
  }
});
const productInputDate = document.querySelector(
  ".tab-content-input_delivery-date"
);
const productInputDeliveryVer = document.querySelector(
  ".tab-content-input_delivery-ver"
);
const tabsContentFormButton = document.querySelector(
  ".tabs-content-form-button"
);
let tabContentTotalCount = document.querySelector(
  ".tab-content-input_cart-count-total"
);
let tabContentTotalPrice = document.querySelector(
  ".tab-content-input_cart-pirce-total"
);



// ТАБЫ
const tabs = document.querySelectorAll(".tabs-tab");
const tabsContent = document.querySelectorAll(".tab-content");
tabs.forEach((tab, index) => {
  tab.addEventListener("click", function () {
    tabs.forEach((tab) => tab.classList.remove("active"));
    tab.classList.add("active");
    tabsContent.forEach((content) => {
      content.classList.remove("active");
    });
    tabsContent[index].classList.add("active");
  });
});



{/* <input
value="${productInputName.value}"
disabled
type="text"
name="cart_product_name_${productsCount}"
id="cart_product_name_${productsCount}"
class="tab-content-input tab-content-input_cart tab-content-input_cart-product-name"
/>
<input
  value="${productInputCount.value}"
  disabled="Кол-во товара"
  type="text"
  name="cart_product_count_${productsCount}"
  id="cart_product_count_${productsCount}"
  class="tab-content-input tab-content-input_cart tab-content-input_cart-product-count"
/>
<input
  value="${productInputDate.value}"
  disabled
  type="text"
  name="cart_product_delivery-date_${productsCount}"
  id="cart_product_delivery-date_${productsCount}"
  class="tab-content-input tab-content-input_cart tab-content-input_cart-delivery-date"
/>
<input
  value="${productInputDeliveryVer.value}"
  disabled
  type="text"
  name="cart_product_delivery-ver_${productsCount}"
  id="cart_product_delivery-ver_${productsCount}"
  class="tab-content-input tab-content-input_cart tab-content-input_cart-delivery-ver"
/>
<input
  value="${productInputPrice.value}"
  disabled
  type="text"
  name="cart_product-price_${productsCount}"
  id="cart_product-price_${productsCount}"
  class="tab-content-input tab-content-input_cart tab-content-input_cart-product-price" */}