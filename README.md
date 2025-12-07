# BitPredict: Digital Currency Insight Program  

## Requirements  
Python 3.11.x  
Streamlit  
CCXT  
Matplotlib  
NetworkX  
Numpy  
Pandas  
## Instructions  
1. Clone the repository, download as ZIP and extract all in your computer.
2. Run requirements.txt (located in Code Folder) in command prompt by copying this text `py -m pip install -r` or `python -m pip install -r`, then drag and drop requirements.txt into command prompt so the filepath is perfectly copied.
Examples:
- `py -m pip install -r requirements.txt`
- `python -m pip install -r requirements.txt`
- `py -m pip install -r (Filepath of requirements.txt)`
- `python -m pip install -r (Filepath of requirements.txt)`

4. Press enter.

# BitPredict Project Proposal
Members:
1. Gartner, Markus Ivan
2. Talatala, Jeremie Leo
3. Ubungen, John Daniel


## Objectives of the Project

The project BitPredict: Digital Currency Insight Program seeks to address/optimize the following:

1. Help users make sensible choices in cryptocurrency investments by using data trends to spotlight the best-performing cryptocurrencies.
2. Inform users on the possible value trajectory of a cryptocurrency and what actions to take accordingly.
3. Suggest possible cryptocurrency investment combinations to boost the portfolio value of users.
4. Educate users on market volatility and the potential risks of investing in cryptocurrency to encourage responsible investments among users.


## Scope and Limitation of the Project

The project covers the following concepts in Discrete Structures 1, namely: graph theory (analyzing connections between different cryptocurrencies), combinatorics (possible investment combinations for a user portfolio), boolean algebra (for decision-making on predictions and classifying trends as upward, downward, or neutral), recurrence relations (for repeated calculations like the moving average of a cryptocurrency), functions (mapping input-output values to supply data for prediction), and set theory (grouping cryptocurrencies based on movement trends), but does not cover number theory, automata theory, advanced counting, proof techniques, advanced relations, complexity analysis, and discrete statistics.

## Programming Language

The project will be made entirely in Python. Core libraries will be used to run the program, and it will use NetworkX and Matplotlib to create and manage crypto correlation graphs (nodes/edges). It will also use Numpy to calculate moving averages, percent changes, and other operations, as well as Itertools for portfolio combinations. Additionally, Pandas will be used for smooth data handling for all imports that will be used. Lastly, for live prices of coins, we will import a cryptocurrency API called CCXT or CryptoCurrency eXchange Trading instead of having sample prices.  

# Project Timeline for BitPredict  
## Week 1 (Aug 31–Sept 6) → Ideation & Selection
- [x] **Brainstormed ideas** for the Discrete Structures final project.
- [x] Created a Google Doc to organize 3 applied-real life project ideas, relevant Discrete Structures concepts, and selected **Python** as the development language.
- [x] Evaluate 3 potential project ideas:
  - Fake News Detection in Social Network
  - Airline and Delivery Scheduling
  - Cryptocurrency Prediction Program
- [x] **All members** chose **Cryptocurrency Prediction Program** as the main project.

## Week 2 (Sept 7-13) → Research Concepts  
- [x] Researched specific **Discrete Structures concepts** applicable to the Cryptocurrency Prediction Program.
- [x] Investigated mathematical models and algorithms suitable for analyzing market trends.

## Week 3 (Sept 14-20) → Project Draft Finalization
- [x] Finalized the draft of **Discrete Structures concepts** to be integrated into the project.
- [x] **Project Confirmation:** Officially locked in the **Cryptocurrency Prediction Program** as the final topic.
- [x] Confirmed **Python** as the primary language for implementation.

## Week 4 (Sept 21-27) → Project Proposal
- [x] Finalized the official project name: **"BitPredict: Digital Currency Insight Program"**.
- [x] Created the **Project Proposal** document containing:
  - Objectives of the project
  - Scope and Limitations of the Project
  - Programming Language
- [x] Prepared and submitted the hard copy of the proposal to the professor in week 5 or 6

## Week 5 (Sept 28-Oct 4) → Proposal Finalization & Tech Stack 
- [x] **Finalized Project Proposal** by integrating specific Discrete Structures concepts:
  - **Graph Theory:** Analyzing connections between different cryptocurrencies (Nodes/Edges).
  - **Combinatorics:** Calculating possible investment combinations for user portfolios.
  - **Boolean Algebra:** Logic for decision-making and trend classification (Upward/Downward/Neutral).
  - **Recurrence Relations:** Handling repeated calculations like moving averages.
  - **Functions:** Mapping input-output values for supply data.
  - **Set Theory:** Grouping cryptocurrencies based on movement trends.
  - *(Note: Explicitly excluded Number Theory, Automata Theory, and Advanced Counting from scope).*
- [x] **Libraries for Python Tech Stack:**
  - **NetworkX & Matplotlib:** For managing and visualizing crypto correlation graphs.
  - **NumPy:** For calculating moving averages and percent changes.
  - **Itertools:** For handling portfolio combinations.
  - **Pandas:** For seamless data handling and manipulation.
  - **CCXT API:** Integrated for retrieving **live cryptocurrency prices** (replacing static sample data).

## Week 6 (Oct 5–11) → Repo Setup 
- [x] **Created the GitHub Repository** for BitPredict.
- [x] Added Collaborators or members of the group in Discrete Structures.
- [x] Initialized the project structure and created a dedicated code folder for the **program prototype**.

## Week 7 (Oct 12-18) → Midterm Break  
- [x] **Paused project development** to focus on Midterm Examinations.

## Week 8 (Oct 19-25) → Thesis Guidelines & Repo Update  
- [x] **Resumed project development** following Midterm Examinations.
- [x] Updated the repository `README.md` to include the full **Project Proposal**.
- [x] Reviewed and documented the **Final Thesis Paper Guidelines**:
  - **Paper Structure:** Introduction, Objectives, Related Work, Methodology (Discrete Concepts), Prototype Design, Results/Findings, Conclusion, and References (min. 3 sources).
  - **Prototype Requirement:** Must present a working simulation addressing the 3 core features.
  - **Presentation Format:** 10–15 minute presentation covering background, problems, discrete concepts, prototype, and results.
    
## Week 9 (Oct 26-Nov 1) → Planning & Task Allocation  
- [x] **Established project deadlines:**
  - Deadlines set for Paper, Prototype Code, and Presentation Slides.
- [x] **Assigned Research Paper sections:**
  - **Gartner, Markus Ivan:** Introduction, Results/Findings.
  - **Ubungen, John Daniel:** Related Work, Prototype Design.
  - **Talatala, Jeremie Leo:** Objectives, Methodology.
  - **All Members:** Conclusion, References.
  - *(Note: Primary owners assigned, but team will assist across all sections).*
- [x] **Defined Coding Strategy:** Adopted a collaborative approach where all members contribute to the prototype code (specific module ownership TBD).
- [X] Added a Tab in the Google Docs for **Final Thesis Paper**

## Week 10 (Nov 2-Nov 8) → Thesis Writing  
- [x] **Progress on the Research Thesis Paper.**
- [x] Conducted detailed research and began writing for individually assigned sections (Introduction, Methodology, Related Work, etc.).

## Week 11 (Nov 9-Nov 15) → Progress on Thesis Writing  
- [x] **Added more information on the Research Thesis Paper.**
- [x] In-text Citations, Bold Text on important text are added.
- [x] Progress with Text Already: Introduction, Objectives, Related Works, Methodology

## Week 12 (Nov 16-Nov 22) → Paper Refinement  
- [x] **Refined and expanded the Research Paper:**
  - **Introduction:** Added comprehensive background information.
  - **Objectives:** Refined and sharpened specific project goals.
  - **Related Works:** Integrated additional research on existing cryptocurrency prediction applications.
  - **Methodology:** Defined key terms and explicitly mapped them to the code implementation.
  - **References:** Added more credible citations to support the research.

## Week 13 (Nov 23–Nov 29) → Finalizing Objectives
- [x] **Significantly revised the "Objectives" section** of the thesis to include specific technical solutions:
  - **Addressing Market Unpredictability:** Specified the method of collecting **7 days of OHLCV data** via the **CCXT** library to classify coin trajectories.
  - **Addressing Portfolio Confusion:** detailed the use of **Combinatorics** to calculate optimal portfolio combinations, citing similar methodologies used by *Puerto et al. (2021)*.
  - **Addressing Connection Identification:** Explained the application of **Graph Theory** (where nodes = coins, edges = correlation strength) to reveal market dependencies, citing *Nguyen et al. (2023)*.
     
## Week 14 (Nov 30-Dec 6) → Start Implementation of BitPredict  
- [x] **Started Coding Phase:** Started writing the core logic for the **BitPredict** application.
- [x] Pushed initial code structure and import statements to the GitHub repository.
- [x] **Defined Dependencies:** Created and pushed `requirements.txt` containing the necessary Python libraries:
  - `ccxt` (Crypto market data)
  - `networkx` (Graph creation)
  - `numpy` (Mathematical operations)
  - `pandas` (Data handling)
  - `matplotlib` (Plotting graphs)
  - `streamlit` (Web interface/Dashboard)
- [x] Added Instructions on how to run code in ReadMe:
- [x] Created working prototype with graphs, dataframes, and input

## Week 15 (Dec 7–13) → Prototype Completion & Refinement
- [x] **Completed the BitPredict Prototype** implementation, ensuring all targeted Discrete Structures concepts were integrated:
  - **Graph Theory** (Market correlations)
  - **Set Theory** (Grouping)
  - **Combinatorics** (Portfolio options)
  - **Propositional Logic** (Decision making)
- [x] **Finalized UI/UX Design:** Integrated the **Final Logo**, custom background, and definitive color palette.
- [x] **Methodology Pivot:** Officially changed the calculation method from Cumulative/Compound to **Moving Average** (Final).
- [x] **Documentation & Presentation:**
  - Started revising the **Research Paper** to align with the finished prototype strictly.
  - Began drafting the **Presentation Slides** for the final defense.
     
  

 

