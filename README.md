<a id="readme-top"></a>
<div align="center">
  <h1 align="center">Latin Numerals Web Translator & Quiz</h1>

  <p align="center">
    Ένα fullstack web project για μετάφραση κι εκμάθηση λατινικών αριθμών μέσω διαδραστικού frontend και RESTful API!
  </p>

  Δείτε την εφαρμογή με το frontend <a href="https://latin-numerals-site.onrender.com">εδώ</a>. Για το Swagger UI (API docs) δείτε <a href="https://latin-numerals-API.onrender.com/docs">εδώ</a>.
</div>

## Περιεχόμενα
- [Περιγραφή Project](#περιγραφή-project)
- [Οδηγίες Εγκατάστασης](#οδηγίες-εγκατάστασης)
- [API Endpoints](#api-endpoints)
- [Χρήση](#χρήση)
- [Μελλοντικές Προσθήκες](#μελλοντικές-προσθήκες)
- [Επικοινωνία](#επικοινωνία)
- [License](#license)

## Περιγραφή Project 

Το project είναι μία web εφαρμογή με backend API σε Python (FastAPI) και frontend με HTML, CSS και JavaScript, που επιτρέπει στον χρήστη:

- Να μεταφράζει λατινικούς αριθμούς σε/από το δεκαδικό σύστημα.
- Να ενημερωθεί για τους κανόνες σύνταξης λατινικών αριθμών.
- Να δοκιμάσει τις γνώσεις του μέσω Quiz μετάφρασης.

Η εφαρμογή έχει ανεβεί στο Render και είναι πλήρως λειτουργική.

### Τεχνολογίες και βιβλιοθήκες που χρησιμοποιήθηκαν:

### Backend:

<a href="https://python.org/"> <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54&style=plastic" alt="Python-Logo" width=100px/></a>

<a href="https://fastapi.tiangolo.com/"> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&style=plastic" alt="FastAPI-Logo" width=100px/></a>

<a href="https://docs.pydantic.dev/latest/"> <img src="https://img.shields.io/badge/%20-Pydantic-E92063?logo=pydantic&logoColor=white-Pydantic&style=plastic" alt="Pydantic-Logo" width=100px height=30px/></a>

<a href="https://www.uvicorn.org/"><img src="https://www.uvicorn.org/uvicorn.png" alt="Uvicorn-Logo" width="35px"/><img src="https://img.shields.io/badge/Uvicorn-blue" alt="Uvicorn-Logo-Text" width=80px></a>

<a href="https://docs.pytest.org/en/stable/"> <img src="https://img.shields.io/badge/-PyTest-3670A0?logo=pytest&logoColor=white&style=plastic" alt="Pytest-Logo" width=100px/></a>

--------

#### Frontend:

<a href="https://www.w3schools.com/html/"> <img src="https://img.shields.io/badge/%20-HTML-blue?logo=HTML5&logoColor=white-HTML&style=plastic" alt="HTML-Logo" width=100px/></a>

<a href="https://www.w3schools.com/css/"> <img src="https://img.shields.io/badge/%20-CSS-663399?logo=CSS&logoColor=white-CSS&style=plastic" alt="CSS-Logo" width=90px/></a>

<a href="https://www.javascript.com/"> <img src="https://img.shields.io/badge/-JavaScript-blue?logo=javascript&style=plastic" alt="JS-Logo" width=120px height=30px/></a>


### Αρχεία του Project

- app/api.py:
  > Ορίζει τα /translate, /quiz_query και /quiz_answer endpoints.
- app/logic.py:
  > Περιέχει όλη τη λογική μετατροπών & διαχείριση απαντήσεων quiz.
- app/main.py:
  > FastAPI app & router include.
- frontend/:
  > Αρχεία .html για home, translator, quiz & rules, αρχεία .css & .js.
- tests/test_api.py:
  > Pytest tests για το API
- requirements.txt:
  > Εξαρτήσεις backend
- .gitignore:
  > Αγνοεί τα αρχεία venv/, .env του virtual environment και __pycache__/ του SpyderIDE.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Οδηγίες Εγκατάστασης

**Backend (API)**

1. Clone του repo
   ```sh
   git clone https://github.com/BlackBaron94/Latin-Numerals-API.git
   ```

2. Αλλαγή directory
   ```sh
   cd Latin-Numerals-API
   ```

3. Δημιουργία virtual environments
   ```sh
   python -m venv venv
   ```
   
4. Ενεργοποίηση venv
   ```sh
   source venv/bin/activate 
   ```
   ή αλλιώς για Windows
   ```sh
   venv\Scripts\activate
   ```

5. Εγκατάσταση προαπαιτουμένων
   ```sh
   pip install -r requirements.txt
   ```

6. Run
   ```sh
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

Το Swagger UI βρίσκεται στη διεύθυνση [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

**Frontend (Static Site)**

1. Clone του repo
   ```sh
   git clone https://github.com/BlackBaron94/Latin-Numerals-API.git
   ```
2. Άνοιγμα του αρχείου frontend/index.html με browser και περιήγηση.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API Endpoints

### `POST /translate`

Μεταφράζει τον αριθμό που δίνεται σύμφωνα με το direction.

**Request**

| Πεδίο  | Τύπος  | Περιγραφή  |
|---|---|---|
| `user_input`  | string | Λατινικός αριθμός ή δεκαδικός σε string |
| `direction`  | string | `"Latin to Decimal"` ή `"Decimal to Latin"` |

**Response**
| Πεδίο | Τύπος  | Περιγραφή  |
|---|---|---|
| `result` | string | Αριθμός που εισήχθη και μετάφρασή του |

<details>
  <summary>Παράδειγμα /translate</summary>
  
`Request`

```json
{
  "user_input": "MMXXV",
  "direction": "Latin to Decimal"
}
```

`Response`

```json
{
  "result": "Result: MMXXV is 2025"
}
```
</details>

--------

### `GET /quiz_query`

Επιστρέφει τυχαίο αριθμό ως ερώτηση μετάφρασης για το Quiz, 50% πιθανότητα για λατινικό και 50% για δεκαδικό αριθμό, στο εύρος 1-3999. 


**Response**

| Πεδίο  | Τύπος  | Περιγραφή  |
|---|---|---|
| `number`  | string | Τυχαίος αριθμός 1-3999 σε λατινικό ή δεκαδικό σύστημα |

<details>
  <summary>Παράδειγμα /quiz_query</summary>

`Response`

```json
{
  "number": "MCMXCIV"
}
```
</details>

--------

### `POST /quiz_answer`

Ελέγχει αν η απάντηση είναι σωστή και κάνει τις απαραίτητες αλλαγές στο streak συνεχόμενων σωστών απαντήσεων.

**Request**

| Πεδίο  | Τύπος  | Περιγραφή  |
|---|---|---|
| `question_number`  | string  | Αριθμός ερώτησης quiz  |
| `user_input`  | string | Απάντηση χρήστη για μετάφραση αριθμού ερώτησης quiz |
| `quiz_streak`  | integer | Τρέχων αριθμός συνεχόμενων σωστών απαντήσεων quiz |


**Response**

| Πεδίο  | Τύπος  | Περιγραφή  |
|---|---|---|
| `result`  | string  | Μήνυμα σωστής/εσφαλμένης απάντησης  |
| `quiz_streak`  | integer | Νέος αριθμός συνεχόμενων σωστών απαντήσεων quiz |

<details>
  <summary>Παράδειγμα /quiz_answer</summary>
  
`Request`

```json
{
  "question_number": "2012",
  "user_input": "MMXII",
  "quiz_streak": 4
}
```

`Response`

```json
{
  "result": "Your answer is correct!<br>2012 is MMXII<br>5 correct answers streak!",
  "quiz_streak": 5
}
```
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Χρήση

Υπάρχει διαθέσιμο short video demo του API και του Web App <a href="https://drive.google.com/file/d/18Q37BlkLpucUDJbaBSIKAfruFPdDpxsf/view?usp=drive_link">εδώ</a>.

**API**

Δέχεται POST /translate, /quiz_answer και GET /quiz_query.

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-API/Swagger-UI.jpg" alt="Swagger-UI" width="750"/>
</div>

**Frontend**

1. Home - Βασικό μενού με βασική επεξήγηση των λειτουργιών.

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-API/Home-page.jpg" alt="Home-page" width="750"/>
</div>

2. Translator - Λαμβάνει αριθμό, επιλογή κατεύθυνση μετάφρασης από τις 2 διαθέσιμες επιλογές, και μεταφράζει με click στο Translate/Enter.

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-API/Translator-Page.jpg" alt="Translator-Page" width="750"/>
</div>

3. Quiz - Εμφανίζει τυχαίο αριθμό, είτε σε λατινικό αριθμό είτε σε δεκαδικό και δέχεται απάντηση με εισαγωγή και click στο Submit/Enter.

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-API/Quiz-Page.jpg" alt="Quiz-Page" width="750"/>
</div>

4. Rules - Εμφανίζει πίνακα με αντιστοίχιση του κάθε λατινικού αριθμού με δεκαδικό και τους κανόνες γραφής και ανάγνωσης λατινικών αριθμών.

<div align="center">
    <img src="https://raw.githubusercontent.com/BlackBaron94/images/main/Latin-Numerals-API/Rules-Page.jpg" alt="Rules-Page" width="750"/>
</div>

<i> **Σημείωση:**  
 Το API του Render μπορεί να χρειαστεί 30–50 δευτερόλεπτα για να ξυπνήσει και να απαντήσει.
 Αν δείτε "Now loading result...", παρακαλώ περιμένετε πριν ανανεώσετε, δουλεύει και θέλει λίγο χρόνο.</i>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Μελλοντικές Προσθήκες

- [X] Δημιουργία υπολοίπων λειτουργιών πλην μεταφραστή με ανάλογες σελίδες.
- [X] Auto-deploy on Push.
- [ ] Ετοιμασία tests με pytest για το API.
- [ ] Responsive UI με burger-type menu.
- [ ] Pagination & history για quiz.
- [ ] Authentication & API key support.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Επικοινωνία

Γιώργος Τσολακίδης - [Linked In: Giorgos Tsolakidis](https://www.linkedin.com/in/black-baron/) - black_baron94@hotmail.com 

Project Link: [Latin Numerals API](https://github.com/BlackBaron94/Latin-Numerals-API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License


This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
