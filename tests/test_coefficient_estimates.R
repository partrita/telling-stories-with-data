test_that("계수 확인", { # 한국어: 계수 확인
  expect_gt(sim_run_data_rain_model$coefficients[3], 0) # 한국어: 세 번째 계수가 0보다 큰지 확인
  expect_lt(sim_run_data_rain_model$coefficients[3], 20) # 한국어: 세 번째 계수가 20보다 작은지 확인
})