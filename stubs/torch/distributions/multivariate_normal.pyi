# Stubs for torch.distributions.multivariate_normal (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.distribution import Distribution
from typing import Any, Optional

class MultivariateNormal(Distribution):
    arg_constraints: Any = ...
    support: Any = ...
    has_rsample: bool = ...
    loc: Any = ...
    covariance_matrix: Any = ...
    def __init__(self, loc: Any, covariance_matrix: Optional[Any] = ..., precision_matrix: Optional[Any] = ..., scale_tril: Optional[Any] = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    def scale_tril(self): ...
    def covariance_matrix(self): ...
    def precision_matrix(self): ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def rsample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...
    def entropy(self): ...