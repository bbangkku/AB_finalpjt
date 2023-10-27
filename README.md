# 금융상품추천_최종프로젝트

# 주제 : 금융 추천 페이지


## 참고페이지
1. [마이뱅크](https://misaving.mibank.me/deposit)
2. [금융감독원 오픈API](https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029)
3. [한국수출입은행 환율정보API](https://www.data.go.kr/data/3068846/openapi.do)
4. [Kakao Maps API](https://apis.map.kakao.com/)
5. [은행연합회 소비자 포털](https://meeting.ssafy.com/s09p01a2/pl/qtm19uowtbnktde443qi4hwfha)
6. [JSON 데이터 Prettier](https://jsonviewer.stack.hu/)
7. [Bank Salad](https://www.banksalad.com/?utm_source=GoogleSA&utm_medium=banksalad&utm_campaign=ALL_WEB_BANKSALAD&utm_content=BRAND_BANKSALAD&utm_term=%EB%B1%85%ED%81%AC%EC%83%90%EB%9F%AC%EB%93%9C&gclid=CjwKCAjw04yjBhApEiwAJcvNoT160Yg-fmpf9Uzc7qPYihQvav9PcOlCpyRJ_N8hx4JegpgPOUGgsRoClcIQAvD_BwE)
8. [vuetify](./https://v2.vuetifyjs.com/en/getting-started/installation/#vue-ui-install)
9. [boardmix](https://boardmix.com/kr/)



## 필수요구사항

1. 메인페이지

2. 회원 커스터마이징
- 필수 포함 필드 (유저이름, 이메일, 가입할 상품 목록 저장필드)

3. 예적금 금리비교 - 데이터 저장
- 데이터 DB저장

4. 환율계산기
- 국가 선택 기능
- 원화 입력 -> 선택한 국가의 통화로 변환된 값 출력
- 타국 통화 입력 -> 원화로 변환된 값 출력



## 기능목록
- 메인페이지(소개)

- User(CRUD)
- 예적금금리데이터가공(API활용) (예시 : 금융상품통합비교공시 API)
   - 데이터 저장
   - 전체 조회
   - 상세 조회
   - 도전 과제(내가 가입한 상품 변경사항 e-mail로 받기)

- 환율 계산기(API활용 2) (한국수출입은행 환율정보 API)

- 근처 은행 검색(API활용 3) (Kakao Maps API)

- 게시판
  - 게시글
    - 상세 조회
    - 게시글 생성
    - 게시글 수정
    - 게시글 삭제
  - 댓글
    - 게시글별 댓글 조회
    - 게시글 수정
    - 게시글 삭제

- 프로필 페이지
  - 사용자 정보
  - 가입한 상품정보
    - 개별 상품 삭제
    - 전체 상품 삭제
  - 가입한 상품의 금리 비교 차트 
  - 금융 상품 추천 알고리즘 구현페이지
    - K-Means Clustering 알고리즘 사용
- README(사항)
> <br>
> I. 팀원 정보 및 업무 분담 내역 <br>
> II. 설계 내용(아키텍처 등) 및 실제 구현 정도<br>
> III. 데이터베이스 모델링(ERD)<br>
> IV. 금융 상품 추천 알고리즘에 대한 기술적 설명<br>
> V. 서비스 대표 기능들에 대한 설명<br>
> VI. 기타(느낀 점, 후기 등)<br>
> <br>

## 회의록
> [노션 링크 ( 하루하루 기록 )](https://flashy-poppy-f10.notion.site/30176ca4cbe14e0d9ffa2a0b1a2049cc?v=9b1185e9f3cb4c46bb03361c5ddf053e&pvs=4)

