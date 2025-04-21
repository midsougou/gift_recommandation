# Gift Recommendation with Python and Streamlit

This project is a web application for gift recommendations. It allows the user to provide information about the gift recipient, and in return, the application suggests gifts that might suit the recipient based on similar users. In addition to receiving recommendations, the user can help improve future results of our interface. Thus, a user who is not satisfied can indicate it and also specify the gift they ultimately chose.

## Prerequisites

- Python 3.7
- Streamlit
- Pandas

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:
```
pip install streamlit pandas
```

## Usage

To launch the application, run the following command in your terminal:
```
streamlit run main.py
```

Once the application is running, you can interact with it by answering questions about the gift recipient:

1. Choose the status type: **Recommend** or **Experience Feedback**.
2. Answer the questions about the recipient, such as gender, age, occasion, favorite place, passion, favorite color, favorite drink, favorite animal, and a word that represents the recipient.
3. For the `Recommend` function, the application will then suggest the top 5 gifts based on similar users.
4. For the `Experience Feedback` function, you can also provide a gift you received and give your preferences to enrich the database.

## Data

The data used for recommendations is stored in a CSV file named `db_test.csv`. This file contains the following columns:

- user_id: user identifier
- recipient: type of recipient (Friend, Family, Partner, Myself, Colleague)
- gender: recipient's gender (Male, Female)
- age: recipient's age
- occasion: occasion for giving the gift (Wedding, Birthday, Christmas, Professional, Special occasion)
- place: recipient’s favorite vacation destination
- passion: recipient’s passion (Video games, Music, Movies, Sports, Reading)
- color: recipient’s favorite color (Blue, Red, Black, White, Green)
- drink: recipient’s favorite drink (Coffee, Tea, Soft drink, Water, Juice)
- animal: recipient’s favorite animal (Koala, Turtle, Dolphin, Lion, Seagull)
- word: a word that represents the recipient (Reserved, Independent, Romantic, Relaxed, Hardworking)
- item: gift recommended or received by the recipient

## Contributions

Contributions to this project are welcome. If you find bugs, potential improvements, or have ideas to extend the features, feel free to let me know.

---

Thank you for using this gift recommendation application. We hope it helps you find the perfect gift for your loved ones!
