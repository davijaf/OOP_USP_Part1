public class Vehicle {
	private int yearOfManufacture;
	private String model;
	private String brand;

	Vehicle(int adf, String m, String ma){
	yearOfManufacture = adf;
	model = m;
	brand = ma;
	}

	public int getManufactureYear() {
	return yearOfManufacture;
	}

	public String model() {
	return model;
	}

	public String brand() {
	return brand;
	}

	public void setYearOfManufacture(int yearOfManufacture) {
	this.yearOfManufacture = yearOfManufacture;
	}

	public void setModel(String model) {
	this.model = model;
	}

	public void setMark(String brand) {
	this.brand = brand;
	}
	}