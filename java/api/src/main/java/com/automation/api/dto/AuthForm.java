package com.automation.api.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Setter
@Getter
@Builder
@ToString
public class AuthForm {
    private String username, password, accessToken, refreshToken;
}
