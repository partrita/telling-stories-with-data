test_that("클래스 확인", { # 한국어: 클래스 확인
  expect_type(sim_run_data$marathon_time, "double") # 한국어: 마라톤 시간의 유형이 double인지 확인
  expect_type(sim_run_data$five_km_time, "double") # 한국어: 5km 시간의 유형이 double인지 확인
  expect_type(sim_run_data$was_raining, "character") # 한국어: 비가 왔는지 여부의 유형이 character인지 확인
})