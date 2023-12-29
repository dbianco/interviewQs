package com.codeame;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Ejercicio1Test {

    private Ejercicio1 ejercicio1;

    @Before
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