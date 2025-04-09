# Payment System for Highridge Construction Company in R

generate_workers <- function(num_workers = 400) {
  first_names <- c("James", "John", "Robert", "Michael", "William", 
                   "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth")
  last_names <- c("Smith", "Johnson", "Williams", "Brown", "Jones", 
                  "Miller", "Davis", "Garcia", "Rodriguez", "Wilson")
  genders <- c("Male", "Female")
  departments <- c("Carpentry", "Masonry", "Plumbing", "Electrical", "Landscaping")
  
  workers <- data.frame(
    id = paste0("EMP", 1000:(1000 + num_workers - 1)),
    first_name = sample(first_names, num_workers, replace = TRUE),
    last_name = sample(last_names, num_workers, replace = TRUE),
    gender = sample(genders, num_workers, replace = TRUE),
    department = sample(departments, num_workers, replace = TRUE),
    hours_worked = sample(30:60, num_workers, replace = TRUE),
    hourly_rate = round(runif(num_workers, min = 15, max = 50), 2),
    stringsAsFactors = FALSE
  )
  
  return(workers)
}

calculate_salary <- function(hours, rate) {
  regular_hours <- pmin(hours, 40)
  overtime_hours <- pmax(hours - 40, 0)
  salary <- (regular_hours * rate) + (overtime_hours * rate * 1.5)
  return(round(salary, 2))
}

determine_employee_level <- function(salary, gender) {
  level <- ifelse(
    salary > 10000 & salary < 20000,
    "A1",
    ifelse(
      salary > 7500 & salary < 30000 & gender == "Female",
      "A5-F",
      "B2"  # Default level
    )
  )
  return(level)
}

generate_payment_slips <- function(workers) {
  tryCatch({
    payment_slips <- data.frame(
      employee_id = workers$id,
      name = paste(workers$first_name, workers$last_name),
      gender = workers$gender,
      department = workers$department,
      hours_worked = workers$hours_worked,
      hourly_rate = workers$hourly_rate,
      weekly_salary = calculate_salary(workers$hours_worked, workers$hourly_rate),
      employee_level = determine_employee_level(
        calculate_salary(workers$hours_worked, workers$hourly_rate),
        workers$gender
      ),
      payment_date = format(Sys.Date(), "%Y-%m-%d"),
      stringsAsFactors = FALSE
    )
    return(payment_slips)
  }, error = function(e) {
    message(paste("Error generating payment slips:", e$message))
    return(NULL)
  })
}

export_to_csv <- function(payment_slips, filename = "payment_slips_r.csv") {
  tryCatch({
    write.csv(payment_slips, file = filename, row.names = FALSE)
    message(paste("Payment slips exported to", filename))
  }, error = function(e) {
    message(paste("Error exporting to CSV:", e$message))
  })
}

# Main execution
tryCatch({
  workers <- generate_workers()
  payment_slips <- generate_payment_slips(workers)
  if (!is.null(payment_slips)) {
    export_to_csv(payment_slips)
    message("Payment slip generation completed successfully!")
  }
}, error = function(e) {
  message(paste("An error occurred in the payment system:", e$message))
})
