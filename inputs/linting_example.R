SIMULATED_DATA <-
  tibble(
    Division = c(1:150,151), # 예시: 선거구 ID
    Party = sample(
      x = c('Liberal'), # 예시: 정당명
      size = 151, # 예시: 데이터 크기
      replace = T # 예시: 복원 추출 여부
    ))