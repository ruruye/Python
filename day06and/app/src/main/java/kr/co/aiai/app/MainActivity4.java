package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class MainActivity4 extends AppCompatActivity {

    EditText et1, et2, et3, et4, et5, et6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        et3 = findViewById(R.id.et3);
        et4 = findViewById(R.id.et4);
        et5 = findViewById(R.id.et5);
        et6 = findViewById(R.id.et6);

        Button btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();

            }
        });
    }

    public void myclick() {
        int[] arr45 = new int[45];
        for(int i=0; i<arr45.length; i++) {
            arr45[i]=i+1;
        }

        for(int i=0; i<1000; i++) {
            int rnd = (int)(Math.random()*45);
            int a = arr45[0];
            arr45[0] = arr45[rnd];
            arr45[rnd] = a;
        }

        et1.setText(arr45[0]+"");
        et2.setText(arr45[1]+"");
        et3.setText(arr45[2]+"");
        et4.setText(arr45[3]+"");
        et5.setText(arr45[4]+"");
        et6.setText(arr45[5]+"");

    }

}