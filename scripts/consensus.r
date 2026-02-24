library(cancensus)
library(tidyverse)

# 1. API 키 설정 (cancensus 전용 방식)
# 실제 키를 따옴표 안에 입력하세요.
options(cancensus.api_key = "")

# 2. 캐시 경로 설정 (경고 메시지 해결 및 성능 향상)
# 현재 작업 디렉토리에 'cache' 폴더를 생성하여 사용합니다.
options(cancensus.cache_path = "./cache")

# 3. 온타리오주 인구 데이터 불러오기
# vectors "v_CA16_1"은 2016년 총 인구수를 의미합니다.
ontario_population <- get_census(
  dataset = "CA16",
  regions = list(PR = "35"),
  vectors = c("v_CA16_1"),
  level = "Regions",
  quiet = TRUE
)

# 4. 결과 출력 및 저장
print(ontario_population)
write_csv(ontario_population, "census_population.csv")

us_ave_household_size_2010 <-
  get_decennial(
    geography = "state",
    variables = c("H012001", "H012002", "H012003"),
    year = 2010
  )

write_csv(us_ave_household_size_2010, "census_household_size.csv")