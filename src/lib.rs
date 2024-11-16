use pyo3::prelude::*;
use std::fs::File;
use std::io::Read;

/// Say hello
#[pyfunction]
fn say_hello(name: String, conf: String) -> PyResult<String> {
    Ok(format!("Hello, {}!, Welcome to {}", name, conf))
}
/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Give are gistration list and check if name is in it
#[pyfunction]
fn check_reg(filename: String, name: String) -> PyResult<String> {
    let mut file = File::open(filename).expect("File not exist");
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    if contents.contains(&name) {
        Ok("You are registered!".to_string())
    } else {
        Ok("Sorry you are not in our list!".to_string())
    }
}
/// A Python module implemented in Rust.
#[pymodule]
fn pyo3_101(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(say_hello, m)?)?;
    m.add_function(wrap_pyfunction!(check_reg, m)?)?;
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
