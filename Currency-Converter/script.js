function loadCurrencies() {
	let baseCurrency=document.querySelector("#baseCurrency").value;
	
	 if(!baseCurrency || baseCurrency==="") {
		alert("Bank Value supplied");
		return;
	}

	var queryURL = `https://exchangeratesapi.io/api/latest?base=${baseCurrency}`;
	
	fetch(queryURL)
	.then(function(response) {
		return response.json();
	})
	.then (function (result) {
		displayCurrencyResult(result);
	})
	.catch (function(error) {
		alert("Something Went Wrong");
		console.log(error.message);
	
	}); 
}

function displayCurrencyResult(result) {

	console.log(result);
	
	let msgDiv=document.querySelector("#message");
	let div=document.querySelector("#rates");
	
	
		
		div.innerHTML="";
		msgDiv.innerHTML=`<div class="">`;
		
		
	
	
		
		
		for(let key=0;key<result.length;key++) {
			
	
	let rateDiv=`<div class="jumbotron" style="text-align:center">
				  <h1>${key}</h1>
				  <h3 style="color:blue">${result.rates[key]}</h3>
				  </div>`;
				 
	
	$("#rates").append(rateDiv);
		}
		
	console.log(result);
}