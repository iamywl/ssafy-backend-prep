package com.ssafy.sample.model.dto;

/////////////////////////////////////
/// --- 수정할 코드가 없습니다.--------///
/////////////////////////////////////
public class Gear {


    private String code;
    private String name;
    private Integer price;
    private String brand;
    private String color;

    // 기본 생성자
    public Gear() {}

    // 전체 필드 생성자 (신규 등록 및 조회 공통 사용)
    public Gear(String code, String name, Integer price, String brand, String color) {
        this.code = code;
        this.name = name;
        this.price = price;
        this.brand = brand;
        this.color = color;
    }

    // Getter / Setter
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getPrice() {
        return price;
    }

    public void setPrice(Integer price) {
        this.price = price;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return "Gear [code=" + code + ", name=" + name + ", price=" + price + ", brand=" + brand + ", color=" + color + "]";
    }
}