public class Car extends Vehicle {
	private int cylinders;


	public String toString() {
	return "Car manufactured in " + getManufactureYear() + " with " + cylinders + " cylinder capacity!";
	}

	Car(int year, String model, String brand, int cylinders) {
	super (year, model, brand);
	this.cylinders = cylinders;
	}

	public static void main(String args[]) {
	Car fordMoustache = new Car(1910,"mustache","Ford",2900);
	System.out.println("The vehicle created was: " + fordMoustache);
	}
	}