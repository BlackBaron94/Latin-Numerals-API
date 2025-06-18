let streak = Number(sessionStorage.getItem("streak")) || 0;

async function translate_clicked() {
	const input = document.getElementById("input").value;
	const direction = document.getElementById("direction").value;
	const resultEl = document.getElementById("result");
	resultEl.textContent = "Now loading result...";
	
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

async function submit_answer_clicked() {
	const question_number = document.getElementById("question_number").textContent;
	const input = document.getElementById("input").value;
	const resultEl = document.getElementById("result");
	resultEl.textContent = "Now loading result...";
	
	try{
		const res = await fetch("https://latin-numerals-api.onrender.com/quiz_answer", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({question_number, input, streak}),
	});
		const data =  await res.json();
		resultEl.textContent = data.result;
		streak = data.streak;
		sessionStorage.setItem("streak", streak);
	} catch (e) {
		resultEl.textContent = "Error: " + e.message;
	}
	
}

document.addEventListener("DOMContentLoaded", () => {
  const questionEl = document.getElementById("question_number");
  if (!questionEl) return; // Μην κάνεις τίποτα αν δεν είναι quiz page

  fetch("https://latin-numerals-api.onrender.com/quiz_query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({})
  })
  .then(response => {
    if (!response.ok) {
      questionEl.textContent = "Network response was not ok";
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then(data => {
    console.log("Random quiz number:", data.number);
    questionEl.textContent = data.number;
  })
  .catch(error => {
    console.error("Fetch error:", error);
  });
});

