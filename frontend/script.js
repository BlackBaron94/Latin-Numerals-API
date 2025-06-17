async function translate_clicked() {
	console.log("potato");
	const input = document.getElementById("input").value;
	const direction = document.getElementById("direction").value;
	const resultEl = document.getElementById("result");
	
	try{
		const res = await fetch("https://latin-numerals-api.onrender.com/translate", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({input, direction}),
		});
		const data  = await res.json();
		resultEl.textContent = data.result;
	} catch (e) {
		resultEl.textContent = "Error: " + e.message;
	}
	
}