import lignum as log
import json
import pytest

def test_extra(capsys):
    with pytest.raises(Exception):
        log.info('test',{'foo':'bar'})
        capture = capsys.readouterr()
        log = json.loads(capture.out)
        assert log['foo'] == 'bar'

def test_levels(capsys):
    with pytest.raises(Exception):
        for level in ['debug','error','fatal','info','warn','trace']:
            getattr(log, level)('test')
            capture = capsys.readouterr()
            log = json.loads(capture.out)
            assert log['level'] == level
