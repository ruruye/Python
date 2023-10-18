package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity5 extends AppCompatActivity {

    EditText et_com,et_mine,et_result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main5);
        et_com = findViewById(R.id.et_com);
        et_mine = findViewById(R.id.et_mine);
        et_result = findViewById(R.id.et_result);
        Button btn = findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();

            }
        });

    }

    public void myclick() {
        String com = "";
        String mine = et_mine.getText().toString();
        String result = "";

        double rnd = Math.random();

        if (rnd > 0.5) {
            com = "홀";
        } else {
            com = "짝";
        }

        if (com.equals(mine)) {
            result = "이김";
        } else {
            result = "짐";
        }

        et_com.setText(com);
        et_result.setText(result);


    }
}