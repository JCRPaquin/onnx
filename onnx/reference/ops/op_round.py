# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunUnaryNum


class Round(OpRunUnaryNum):
    def _run(self, x):  # type: ignore
        return (np.round(x).astype(x.dtype),)
