# Casual Inference
The method by which causes are inferred from the evidence is known as causal inference. In this study, causes are deduced from examination of data from breast cancer diagnosis.


## Objective
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
1. “What will happen if I halve the price of my product?”
2. “Which clients will pay their debts only if I call them?”


## Data
The Data can be downloaded from [kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) or from [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets?name=breast). In the latter you can find even more data that you may explore further. To understand more about the data, and how it is collected we highly recommend reading this paper: (PDF) Breast Cancer Diagnosis and Prognosis Via Linear Programming (researchgate.net).

Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.
Attribute Information:
ID number
Diagnosis (M = malignant, B = benign)
The remaining (3-32)
Ten real-valued features are computed for each cell nucleus:
radius (mean of distances from center to points on the perimeter)
texture (standard deviation of gray-scale values)
Perimeter
Area
smoothness (local variation in radius lengths)
compactness (perimeter^2 / area - 1.0)
concavity (severity of concave portions of the contour)
concave points (number of concave portions of the contour)
Symmetry
fractal dimension ("coastline approximation" - 1)
The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius. All feature values are recorded with four significant digits.
Missing attribute values: none
Class distribution: 357 benign (not cancer), 212 malignant (cancer)


## Contrbutors
- Yididiya Samuel

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[MIT](https://choosealicense.com/licenses/mit/)
