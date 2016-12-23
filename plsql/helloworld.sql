set serveroutput on
declare
    msg varchar2(20) := 'Hello World'
begin
    dbms_output.put_line(msg);
end;
/