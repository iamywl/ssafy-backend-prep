package com.ssafy.exam.model.dto;

import java.io.Serializable;

/*이 파일에서는 수정 할 부분이 없습니다. */

public class Car implements Serializable {
	private String code;
	private String model;
	private Integer price;
	private String vendor;
	private String size;
	
	public Car() {
		// TODO Auto-generated constructor stub
	}

	public Car(String code, String model, Integer price, String vendor, String size) {
		super();
		this.code = code;
		this.model = model;
		this.price = price;
		this.vendor = vendor;
		this.size = size;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public Integer getPrice() {
		return price;
	}

	public void setPrice(Integer price) {
		this.price = price;
	}

	public String getVendor() {
		return vendor;
	}

	public void setVendor(String vendor) {
		this.vendor = vendor;
	}

	public String getSize() {
		return size;
	}

	public void setSize(String size) {
		this.size = size;
	}

	@Override
	public String toString() {
		return "Car [code=" + code + ", model=" + model + ", price=" + price + ", vendor=" + vendor + ", size="
				+ size + "]";
	}
	
	
	
	
	
	

}
