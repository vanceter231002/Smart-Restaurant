let ctr_btn = document.querySelectorAll(".ctr");
let inputs = document.querySelectorAll(".inp");
let notif = document.querySelector(".notif");
let cart = document.querySelector(".cart");
let howMuch = document.querySelector(".how_much");
let item = document.querySelector(".item");
let bought = document.querySelector(".btn_buy");
let buy_now = document.querySelector(".open_cart");
let number = 0;

function update_total()
    {
		if(!document.URL.includes("order"))
		{
			return
		}
		var list= document.getElementsByClassName("food");
		console.log("This is list");
		console.log(list);
		var total_price=0;
		var curr_price=0;
		for (var i = 0; i < list.length ; i++) {
			current_element=list[i];
			price_element=current_element.querySelector("p.price")
			curr_price=parseInt(price_element.innerHTML.slice(0,price_element.innerHTML.length-1));
			quantity=current_element.querySelector("input[title='food_counter']").value;
			console.log(curr_price);
			console.log(quantity);
			quantity=parseInt(quantity);
			total_price=total_price+curr_price*quantity;
		}
		var s="Total Amount: "
		s=s.concat(total_price.toString(),"₹")
		document.getElementById('total_price').innerHTML=s
		console.log(total_price);
	}
update_total();
ctr_btn.forEach((ctrButton) => {
	ctrButton.addEventListener("click", () => {
		let parentCtr = ctrButton.parentElement;
		let child = parentCtr.children[1];
		if (ctrButton.className == "ctr plus") {
			if (child.value === "") {
				child.value = "1";
			} else {
				child.value++;
			}
			
			update_total();
		} else {
			if (child.value > "1") {
				child.value--;
			} else {
				child.value = null;
			}
			update_total();
		}
		if (child.value >= "1") {
			notif.style.display = "inline";
			cart.addEventListener("click", () => {
				window.open("../order", "_self");
			});
			buy_now.addEventListener("click", () => {
				window.open("../order", "_self");
			});
			buy_now.style.transform = `translateY(0%)`;

		} else {
			notif.style.display = "none";
			buy_now.style.transform = `translateY(300%)`;
		}
		if (child.value >= "1") {
			number++;
			localStorage.setItem("number", number);
		}
	});
});

const replace = () => {
	let num = localStorage.getItem("number");
	if (num == 1) {
		item.textContent = "item";
	} else item.textContent = "items";
	howMuch.textContent = num;
};

const rem = () => {
	localStorage.removeItem("number");
};

if (bought)
	bought.addEventListener("click", () => {
		bought.innerHTML = `<div class="lds-ring"><div></div><div></div><div></div><div></div></div>`;
		setTimeout(() => {
			window.open("../thanks", "_self");
		}, 3000);
	});
