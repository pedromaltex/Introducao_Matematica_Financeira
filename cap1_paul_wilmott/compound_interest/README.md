# Compound Interest Calculator💲

A web-based financial calculator built with **Streamlit** that allows users to simulate the growth of investments over time using **compound interest**. It supports both **lump-sum investments** and **recurring contributions** with customizable frequencies.

---

## 🚀 Features

- Calculate **future value** of a lump-sum investment.
- Calculate **future value** of recurring contributions (monthly, yearly, weekly).
- Interactive **line or bar charts** to visualize portfolio growth.
- Easy-to-use **sidebar inputs** to adjust all parameters.

---

## 📷 Demo

![App Screenshot](cap1_paul_wilmott/compound_interest/screenshots/demo.png)  
*Replace this with an actual screenshot or GIF showing the app in action.*

---

## ⚙️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/pedromaltex/Introducao_Matematica_Financeira.git
cd Introducao_Matematica_Financeira/cap1_paul_wilmott/compound_interest
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Then, in the sidebar:

1. Input the initial investment.

2. Specify the contribution amount (if any).

3. Choose the frequency of contributions.

4. Input the interest rate and select its frequency.

5. Select the number of years for the simulation.

6. Click Calculate to view the growth chart.

## 📚 Functions

### `compounded_f_value(i_v, annual_r, t)`

Calculates the **future value of a single lump-sum investment**.

**Parameters:**

- `i_v` (float): Initial investment (present value)  
- `annual_r` (float): Annual interest rate in decimal (e.g., 0.05 for 5%)  
- `t` (int): Number of years  

**Returns:**  
- `float` → Future value of the investment

---

### `compounded_periodic_fvalue(payment, annual_r, m, t)`

Calculates the **future value of recurring contributions** (annuity).

**Parameters:**

- `payment` (float): Contribution made each period  
- `annual_r` (float): Annual interest rate in decimal  
- `m` (int): Number of compounding/contribution periods per year  
- `t` (int): Number of years  

**Returns:**  
- `float` → Future value of the recurring contributions


## 🎨 Visualization

- Uses Plotly to display interactive charts.

- Users can switch between line and bar graphs to visualize growth trajectories.

## 🧮 Example

- Initial investment: $2000

- Monthly contribution: $500

- Annual interest rate: 7%

- Time horizon: 20 years

The app will show the accumulated portfolio value over time in an interactive chart.

## 📄 License

This project is licensed under the MIT License.
Feel free to use and modify it for personal or educational purposes.

## 🙏 Acknowledgements

- Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/).

- Inspired by common financial calculators for teaching compound interest concepts.