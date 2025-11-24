package com.automation.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@Builder
@ToString
public class UserForm {
    @Builder.Default
    private int id = 0;
    
    @Builder.Default
    private int age = 0;
    private String username, password, firstName, lastName, gender, eyeColor, email, image, birthDate; 
}
