'''
개요: 외부모듈
작성자: 진상영
작성일: 2021.03.27
내용: 서드파티모듈(third-party module)
1) 패키지: 모듈의 집합
2) 외부모듈: 패키지에 포함된 모듈 사용
3) 패키지 설치 및 삭제
- 설치: pip install package / ex.numpy(넘파이)
- 삭제: pip uninstall package
'''

import numpy as np
print(np.sum([1,2,3,4,5]))