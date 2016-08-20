I will not terrify you with this term [**Singular Value Decomposition** / **SVD**](https://en.wikipedia.org/wiki/Singular_value_decomposition).
It is nothing but a fancy term for decomposiing a sinlgle matrix into 3 different matrices as:  
`X = U * S * Vt`  
where (technically),    
```
X  = original matrix  
U  = left singular vectors of X  
V  = right singular vectors of X  
Vt = transpose of V  
S = singular diagonal matrix of X  
```

> It is used for dimension reduction and Principal Component Analysis too

Ok!! Those technical names apart. What this means is:

#### The X
**X** is the original matrix of dataset whose columns represent the attributes/dimensions/features and rows represent the point. That is,
each row of X is a vector in that dimension. And, the goal of **SVD** is to reduce these dimensions. 
> In later part of this article, I will mention how that can be achieved.

Say, the columns (attributes) are *mass*, *density*, *volume*, *Fahrenhiet*, *Celsius* and no. of data points is 6.
![x_original](https://drive.google.com/uc?export=view?&id=0B1R9wrwoLnVDU2VJclAwRmpfTjg)


#### The U, V
These are just orthonormal vectors i.e. the columns of **U** and **V** represent unit vectors/axis that are orthogonal to each other.
That is:  
```
U * Ut = Identity  
V * Vt = Identity
```

#### Algorithm
In order to decompose matrix **X**, we have to calculate `X*Xt` and `Xt*X`.
