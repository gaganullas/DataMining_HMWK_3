# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering merges clusters based on proximity, progressively forming a hierarchical structure and effectively mitigating the influence of outliers by grouping them with nearby points.while k-means assigns points to centroids, making it sensitive to outliers influence on centroid positions."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In k-means, the initial placement of centroids is random, leading to varying clusterings in different runs. However, agglomerative hierarchical clustering always produces the same clustering because it follows a deterministic process of merging clusters based on proximity."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is generally more computationally efficient and memory-friendly than agglomerative hierarchical clustering for large datasets, it's not accurate to say it's the most efficient clustering algorithm possible. Other algorithms may outperform k-means under certain conditions or have advantages in specific scenarios."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE of the clustering typically decreases.This is because splitting a cluster into two allows the centroids to better represent the data points within each smaller cluster, resulting in reduced distances between data points and their respective centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "When the Sum of Squared Errors (SSE) decreases during the clustering process in K-means, it means that the data points within each cluster are getting closer to their respective centroids. This implies that the clusters are becoming more cohesive."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "When SSB increases, it means that the centroids are farther apart from each other, indicating more separation between the clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion in k-means clustering typically leads to increased separation, as data points become more tightly clustered within their respective clusters, making the centroids more distinct from each other."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "When clustering data with K-means, the sum of within-cluster sum of squares (SSE) and between-cluster sum of squares (BSS) remains constant, equaling the total sum of squares (TSS)."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Improving cohesion in k-means clustering typically leads to increased separation, as data points become more tightly clustered within their respective clusters, making the centroids more distinct from each other"

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

  
    

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10 * R**2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The centroids in Circle B should move towards the centroid of Circle A and Circle C, due to the uniform distribution of points within each circle. As a result, after convergence, each circle should have 1 centroid, as the centroids would redistribute to balance the points in each circle."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "A will retain its centroid due to the uniform distribution of points within the circle. Circle B, initially having two centroids, may redistribute one of its centroids towards Circle C to balance the distribution of points. Circle C, initially with no centroids, will receive one centroid from Circle B. Therefore, after convergence, each circle will have one centroid."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Given that Circles A and B are much closer to each other, it's likely that the centroid initially in Circle A would move towards the midpoint between Circles A and B during the k-means process. Circle C, being farther away from Circle B, may not influence the redistribution of centroids as much and retains its 2 centroids."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A','Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B are going to be combined because their distance, measured from the furthest right point in A to the furthest left point in B, is shorter than the distance between A and C, as well as between B and C."

    # type: set
    answers["(b)"] =  {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Groups A and C are going to be combined because they have the shortest complete link distance, which is measured between a boundary point of A and the farthest point in C. This distance is shorter than the complete link distances between A and B (measured from the left-most point in A to the right-most point in B) and between B and C (measured from the right-most point in B to the farthest point in C)"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E', 'B', 'F', 'J', 'C', 'L', 'M', 'I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','E','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M' }

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The cluster with the largest clustering entropy is Cluster 4 because it has a more balanced distribution of objects across different classes compared to the other clusters."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It has a dominant class with significantly higher counts compared to the other classes.The dominance of one class within the cluster leads to lower entropy"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The clear and predominant blue color in each diagonal entry indicates a high level of cohesion within clusters.This implies that points within the same cluster are tightly clustered together, maintaining consistent coherence within each cluster."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 are associated with clusters A and C, respectively, distinguished by the varying colors in the off-diagonal entries.Rows 2 and 4 correspond to clusters B and D, respectively, showing similar findings."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Diagonal entries notably exhibit clear and primarily blue characteristics, distinguishing themselves from the others. This indicates a high level of cohesion within clusters B and C"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4, with less defined diagonal entries, display various colors, indicating differing distances from all other clusters.Rows 2 and 3, display two identical colors, indicating equidistant relationships with two clusters while maintaining a greater distance from one cluster."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries exhibit increased clarity and intensity in blue color, indicating strong cohesion within clusters B and C. This uniformity suggests stronger intra-cluster relationships within these clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In every row, two off-diagonal entries have matching colors, while one entry stands out with a different color. This suggests that each cluster is relatively closer to two other clusters compared to the third one."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "All off-diagonal entries show different colors, indicating varying distances from other clusters. A cluster has varying distances from other clusters. The diagonal entry is less defined, suggesting weaker cohesion within this cluster. So it will be Cluster A."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The diagonal entry is clearer, suggesting robust cohesion within this cluster. Two out of three off-diagonal entries have matching colors, indicating equidistant relationships which can be clearly seen in case of B with A and C , B is notably farther from  D. So Row 2 is Cluster B"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The diagonal entry is clearer, suggesting robust cohesion within this cluster. Two out of three off-diagonal entries have matching colors, indicating equidistant relationships which can be clearly seen in case of C with B and D , C is notably farther from  A. So Row 3 is Cluster C"

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "All off-diagonal entries show different colors, indicating varying distances from other clusters. D cluster has varying distances from other clusters(D is closest to C, then B, and farthest from A). The diagonal entry is less defined, suggesting weaker cohesion within this cluster. So it will be Cluster D"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(b)"] = ['Partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['Partitional','fuzzy','complete']

    # type: list
    answers["(d)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(e)"] = ['Partitional','Exclusive','partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "It can also be hierarchical structure ,where students with similar performance levels can be grouped together"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The points in the nose, eyes, and mouth are much closer together than the points between these areas."

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " K-means would find the nose, eyes, and mouth, but the lower density points would also be included"

    # type: string
    answers["(c)"] = "Compute the reciprocal of the density to obtain the new density, then apply DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
