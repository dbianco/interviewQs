package com.codeame;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
public class Ejercicio1Test {

    private Ejercicio1 ejercicio1;

    @BeforeEach
    public void setUp() {
        ejercicio1 = new Ejercicio1();
    }

    @Test
    public void sum13Test1() {
        assertEquals(6,ejercicio1.sum13( new int[]{1, 2, 2, 1}));
    }

    @Test
    public void sum13Test2() {
        assertEquals(2,ejercicio1.sum13( new int[]{1, 1}));
    }

    @Test
    public void sum13Test3() {
        assertEquals(6,ejercicio1.sum13( new int[]{1, 2, 2, 1, 13}));
    }


}