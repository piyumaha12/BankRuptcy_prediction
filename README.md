# Bankruptcy Prediction app deployment using Streamlit
![Smith-Debnam-Articles-and-Insights-68-900x350-c-default](https://user-images.githubusercontent.com/71897685/149876757-aa4be791-5887-403e-82f0-923330694d13.png)

## What is Bankruptcy:
Bankruptcy is a legal process through which people or other entities who cannot repay debts to creditors may seek relief from some or all of their debts. 
There are various reasons  oe factors behind the bankruptcy of company. 

This web app predicts whether a company is getting Bankrupted or Not Bankrupted based on the factors like Industrial Risk, Management Risk, Financial Flexibility, Credibility, Competitiveness, Operating Risk.

### Factors Behind bankruptcy:
1. Industrial Risk :
- It refers to the factors that can impact a particular industry, which can turn affect the companies within the sector. 
- For example a tax increase in the automobile industry may adversely affect the profits of the automobile producers due to the sharp decline in the sales volume.  
- Industries face various types of risks like technological shifts, politically induced tariffs, competitive threats and other reasons.  The mature industries generally have lower industry risk and emerging industries which face higher uncertainty and so higher risk.
2. Management risk :
- This is the risks associated with ineffective, destructive or underperforming management.
- Bad management lead to other problems in company like in funding, employee dissatisfaction, corruption etc.
- Higher the Management risk, higher to probability of bankruptcy.
3. Operational Risk :
- Operational risk is resulting from errors or failed internal process, people and systems of company
- The most important types of operational risk involve breakdowns in internal controls and corporate governance. Such breakdowns can lead to financial losses through error, fraud and corruption.
- Other aspects of operational risk include major failure of information technology systems or events such as major fires or other disasters.
4. Credibility :  
- credibility means to which consumers believe that a firm can design and deliver products and services that satisfy customer needs and wants. 
- These dimensions help to influence consumer attitudes and persuade them to purchase a company's products or services.
- Credibility in business is key in helping your company attract both employees and customers as well as investors. 
- It also help when applying for loans, negotiating terms, troubleshooting production issues or requesting an extension on credit.
5. Competitiveness : 
- Competitiveness is a measure of the ability to compete within a business sector. 
- It is also referred to as the organization's ability to act and react through its financial strength. 
- Competitiveness should be higher for a company,  which tell that the company have a strength of compete with other.
- Higher the competitiveness lower the risk of bankruptcy.
6. Financial Flexibility : 
- Financial flexibility is the measure of an organization’s ability to do what it wants when it wants without compromising the larger financial picture. 
- The company able to make quick decision because of financial flexibility. Hence we can say that the company is financially more strong.
- Higher the financial flexibility, lower the chances of bankruptcy.

**These Factors are divided in to 3 categories: High risk (1), Medium risk (0.5), And Low risk (0)**

This project is binary classification type having two outputs **Bankrupt and Non-Bankrupt**

# Libraries Uses:
The web app was built in Python using the following libraries:

- streamlit
- pandas
- numpy
- scikit-learn
- tensorflow
