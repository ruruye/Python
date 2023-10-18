package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity6 extends AppCompatActivity {

    EditText et;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);

        et = findViewById(R.id.et);
        tv = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String input = et.getText().toString();
                if (!input.isEmpty()) {
                    int number = Integer.parseInt(input);
                    printMultiplicationTable(number);
                }
            }
        });
    }

    private void printMultiplicationTable(int number) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 9; i++) {
            int result = number * i;
            sb.append(number).append(" x ").append(i).append(" = ").append(result).append("\n");
        }
        tv.setText(sb.toString());
    }
}