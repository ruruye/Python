package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity3 extends AppCompatActivity {

    EditText et1 ;
    EditText et2 ;
    EditText et3 ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        et3 = findViewById(R.id.et3);

        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateSum();
            }
        });


    }
    public void calculateSum() {
        String a = et1.getText().toString();
        String b = et2.getText().toString();
        int aa = Integer.parseInt(a);
        int bb = Integer.parseInt(b);


        int sum = 0;
        for (int i = aa; i <= bb; i++) {
            sum += i;
        }

        et3.setText(sum+"");
    }


}