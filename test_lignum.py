import lignum
import json
import pytest

def test_levels(capsys):
    with pytest.raises(Exception):
        log = lignum.Logger()
        for level in ['debug','error','fatal','info','warn','trace']:
            getattr(log, level)('test')
            output = json.loads(capsys.readouterr())
            assert out['level'] == level
            assert out['message'] == 'test'

def test_extra(capsys):
    with pytest.raises(Exception):
        log = lignum.Logger()
        log.info('test', {'foo':'bar'})
        output = json.loads(capsys.readouterr())
        assert out['foo'] == 'bar'
        assert out['level'] == 'info'
        assert out['message'] == 'test'

def test_stdout(capsys):
    with pytest.raises(Exception):
        log = lignum.Logger(sys.stdout)
        for level in ['debug','error','fatal','info','warn','trace']:
            getattr(log, level)('test')
            output = json.loads(capsys.readouterr())
            assert out['level'] == level
            assert out['message'] == 'test'

def test_file(capsys, tmpdir):
    with open(tmpdir.join('log.log'),'w') as f:
        log = lignum.Logger(f)
        log.info('test')
    with open(tmpdir.join('log.log'),'r') as f:
        lines = f.readlines()
        assert 'test' in lines[0]
