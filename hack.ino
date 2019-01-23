#define tp 10
#define ep 13
#define tp2 6
#define ep2 3
int r1,r2,d,c,l=100;
void setup()
{
  Serial.begin(9600);
  pinMode(tp,OUTPUT);
  pinMode(ep, INPUT);
  pinMode(tp2,OUTPUT);
  pinMode(ep2, INPUT);
}
void loop()
{
  int time;
  int dist,dist2;
  digitalWrite(tp,HIGH);
  delayMicroseconds(1000);
  digitalWrite(tp,LOW);
  time = pulseIn(ep,HIGH);
  dist = (time/2)/29.1;
  
  //delay(10);

//for second sensor

digitalWrite(tp2,HIGH);
  delayMicroseconds(1000);
  digitalWrite(tp2,LOW);
  time = pulseIn(ep2,HIGH);
  dist2 = (time/2)/29.1;
  
  if(dist2<100 && dist2 > 0 && dist<100 && dist>0){
 // Serial.print(dist);
  //Serial.print(",");
//  Serial.println(dist2);
  
  //Serial.println("m");

  r1=dist, r2=dist2;
   c=((r1*r1)-(r2*r2)+(l*l))/(2*l);
    d=sqrt((r1*r1)-(c*c));
    
    Serial.print(c);Serial.print(",");Serial.println(d);
  delay(50);
  }
}

