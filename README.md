# multiViewAP
Python code to test the behavior of analogical proportions when focusing on diverse sets of features

# This is related to IPMU 2024 paper: 
**Multiple viewpoint analogical proportions and their weighting** (Henri Prade - Gilles Richard)

1. Download the dataset from https://www.kaggle.com/datasets/devvret/congressional-voting-records
2. Run jupyter notebook ipmu2024.ipynb
3. Feel free to change all parameters like: *number_of_elements* (default 10), the masks *focus0* and *focus1*
4. Then observe the diverse printed numbers
5. Note: Increasing number_of_elements (the number of loaded raws) will necessarily increase the runtime
6. In figure summary.jpg, we provide a screenshot summary of what is computed by the notebook:

   ![summary](https://github.com/gillesirit/multiViewAP/assets/61297905/09ab5dfa-cb1a-4d4b-9059-962b4183b7e1)

   
 – Line 1 provides main information on full dataset, sample size and dimension.
 
 – Line 2 provides the number of pairs and pairs of pairs.
 
 – Line 3 indicates how many analogies we get when focusing on focus0: 10
 
 – Line 4 indicates how many analogies we get when focusing on focus1: 8
 
 – Line 5 indicates how many analogies we get when focusing on focus0 intersection
focus1: we get more than the 2 previous because we have less constraints.

 – Line 6 indicates that with the 10 analogies of line 3, we can build 10 transitive
patterns and they are all effective: this is expected as analogy is transitive when
focusing on the same attributes.

 – Line 7 indicates that with the 8 analogies of line 4, we can build 8 transitive patterns
and they are all effective: this is expected as analogy is transitive when focusing on
the same attributes.

 – Line 8 indicates that we can build 6 transitive patterns between l0 and l1, only 2 are
successful when focusing on focus0 (no transitivity).

 – Line 9 indicates that we can build 6 transitive patterns between l0 and l1, only 2 are
successful when focusing on focus1 (no transitivity).

 – Line 10 indicates that we can build 6 transitive patterns between l0 and l1, all 6
are successful when focusing on focus0 intersection focus1, which is the expected
transitivity.

 – Line 11 provides the profile of the solution for a : b : c : x focusing on focus0.
 
 – Line 12 provides the profile of the solution for a : b : c : x focusing on focus1.
 
 – Line 13 When solving analogical equation with a, b, c above, focusing on focus0,
we get a profile matching 49 profiles of the dataset (no unicity).

 – Line 14 When solving analogical equation with a, b, c above, focusing on focus1,
we get a profile matching 44 profiles of the dataset (no unicity).

Clearly, each test will lead to varying results given that the sample of 10 profiles is
randomly selected.
