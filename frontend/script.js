let quiz_streak = Number(sessionStorage.getItem("quiz_streak")) || 0;

async function translate_clicked() {
	const user_input = document.getElementById("user_input").value;
	const direction = document.getElementById("direction").value;
	const resultEl = document.getElementById("result");
	resultEl.textContent = "Now loading result...";

	try {
		const res = await fetch("https://latin-numerals-api.onrender.com/translate", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ user_input, direction }),
		});

		const data = await res.json();

		resultEl.innerHTML = data.result;
	} catch (e) {
		resultEl.textContent = "Error: " + e.message;
	}
	const input_area = document.getElementById("user_input");
	input_area.value = "";
	input_area.focus();
}


async function submit_answer_clicked() {
	const question_number = document.getElementById("question_number").textContent;
	const user_input = document.getElementById("user_input").value;
	const resultEl = document.getElementById("result");
	resultEl.textContent = "Now loading result...";
	
	try{
		const res = await fetch("https://latin-numerals-api.onrender.com/quiz_answer", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({question_number, user_input, quiz_streak}),
	});
		const data =  await res.json();
		resultEl.innerHTML = data.result;
		quiz_streak = data.quiz_streak;
		sessionStorage.setItem("quiz_streak", quiz_streak);
	} catch (e) {
		resultEl.textContent = "Error: " + e.message;
	}
	fetchNewQuizNumber();
	const input_area = document.getElementById("user_input");
	input_area.value = "";
	input_area.focus();
}

async function fetchNewQuizNumber() {
	const questionEl = document.getElementById("question_number");
	if (!questionEl) return;

	try {
		const res = await fetch("https://latin-numerals-api.onrender.com/quiz_query", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({})
		});

		if (!res.ok) {
			questionEl.textContent = "Network response was not ok";
			throw new Error("Network response was not ok");
		}

		const data = await res.json();
		console.log("Random quiz number:", data.number);
		questionEl.textContent = data.number;

	} catch (error) {
		console.error("Fetch error:", error);
	}
}

document.addEventListener("DOMContentLoaded", () => {
	fetchNewQuizNumber();
});


const inputEl = document.getElementById("input");
if (inputEl) {
  const isTranslatorPage = document.getElementById("direction") !== null;
  const handler = isTranslatorPage ? translate_clicked : submit_answer_clicked;

  inputEl.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handler(); 
    }
  });
}
