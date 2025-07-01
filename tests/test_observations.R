test_that("관측치 수 확인", { # 한국어: 관측치 수 확인
  expect_equal(nrow(sim_run_data), 200) # 한국어: 관측치 수가 200과 같은지 확인
})

test_that("완전성 확인", { # 한국어: 완전성 확인
  expect_true(all(complete.cases(sim_run_data))) # 한국어: 모든 케이스가 완전한지 확인
})