package com.example.user.basiccalc;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class basicCalc extends AppCompatActivity {
EditTest num1,num2;
Button AddButton,SuButton,MulButton,DivButton;
TextView TV;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_basic_calc);
        num1=findViewById(R.id.numOne);
        num2=findViewById(R.id.numTwo);

        AddButton=findViewById(R.id.add_btn);
        AddButton.onClickListener(this);

        SuButton=findViewById(R.id.sub_btn);
        MulButton=findViewById(R.id.mul_btn);
        DivButton=findViewById(R.id.div_btn);
    }
    public class onClic(View v)
    {
        int id=v.getId();
        if(id==R.id.add_btn)
        {
            String str1=num1.getTest().toString();
            String str2=num2.getTest().toString();
            int a=Integer.parseInt(str1);
            int b=Integer.parseInt(str2);
            int c= a+b;
            String R=Sring.valueOf(c);
            TV.setTest(R);

        }
    }
}
