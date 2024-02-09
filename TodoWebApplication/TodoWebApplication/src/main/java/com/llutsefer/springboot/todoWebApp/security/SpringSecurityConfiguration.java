package com.llutsefer.springboot.todoWebApp.security;

import java.util.function.Function;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SpringSecurityConfiguration {


    @Bean
    public InMemoryUserDetailsManager createUserDetailsManager() {

        UserDetails userDetails1 = createNewUser("user", "user");
        UserDetails userDetails2 = createNewUser("llutsefer", "qwerty");

        return new InMemoryUserDetailsManager(userDetails1, userDetails2);
    }

    @Bean
    public PasswordEncoder getBCryptEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.authorizeHttpRequests(
                auth -> auth.anyRequest().authenticated());
        httpSecurity.formLogin(Customizer.withDefaults());
        httpSecurity.csrf().disable();
        httpSecurity.headers().frameOptions().disable();
        return httpSecurity.build();
    }

    private UserDetails createNewUser(String username, String password) {
        Function<String, String> passwordEncoderLambda
                = input -> getBCryptEncoder().encode(input);


        return User.builder()
                .passwordEncoder(passwordEncoderLambda)
                .username(username)
                .password(password)
                .roles("USER", "ADMIN")
                .build();
    }

}